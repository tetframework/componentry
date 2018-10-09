from typing import Optional, Union, Type as Class
from threading import RLock

# TODO: weak dictionary
_class_cast_distance_cache = {}


def _do_calculate_cast_distance(c1, c2):
    if c1 is c2:
        return 0

    try:
        return c1.__mro__.index(c2)
    except ValueError:
        pass

    try:
        return -c2.__mro__.index(c1)
    except ValueError:
        pass

    return None

def class_cast_distance(c1, c2):
    try:
        return _class_cast_distance_cache[c1, c2]
    except KeyError:
        pass

    rv = _class_cast_distance_cache[c1, c2] = _do_calculate_cast_distance(c1, c2)
    return rv


_NOT_FOUND = object()


class ComponentLookupException(KeyError):
    pass


class Registry:
    def __init__(self):
        self.utilities = {}
        self._utility_cache = {}
        self.utility_lock = RLock()

    def register_utility(self,
                         *,
                         component: Union[Class],
                         provided: Union[Class]=None,
                         name: str=''):
        if provided is None:
            provided = object

        with self.utility_lock:
            self.utilities[provided, name] = component
            self._utility_cache = {}

    def unregister_utility(self,
                           *,
                           component: Union[Class]=None,
                           provided: Union[Class]=None,
                           name: str=''):
        with self.utility_lock:
            if self.utilities.get((provided, name)) == component:
                del self.utilities[provided, name]
                self._utility_cache = {}

    def _raw_query_utility(self,
                           *,
                           provided: Union[Class]=None,
                           name: str=''):
        if provided is None:
            provided = object

        try:
            utility = self._utility_cache[(provided, name)]
            if utility is _NOT_FOUND:
                raise ComponentLookupException('No such utility {} {}') from None

            return utility

        except:
            candidates = []

            with self.utility_lock:
                for k, component in self.utilities.items():
                    utility_provided, utility_name = k
                    if utility_name == name:
                        ccd = class_cast_distance(utility_provided, provided)
                        if ccd is not None and ccd >= 0:
                            candidates.append((ccd, component))

                if not candidates:
                    raise ComponentLookupException('No such utility {} {}') from None

                chosen = sorted(candidates, key=lambda x: x[0])[0]
                self._utility_cache[(provided, name)] = chosen
                return chosen

    def query_utility(self,
                      *,
                      provided: Union[Class]=None,
                      name: str=''):
        ccd, found = self._raw_query_utility(provided=provided, name=name)
        return found
