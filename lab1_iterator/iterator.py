"""Implementation of the Iterator pattern for tourist places"""

from collections.abc import Iterable, Iterator


class TouristPlacesIterator(Iterator):
    """Basic iterator of tourist places"""
    def __init__(self, tourist_places: list):
        self.tourist_places = tourist_places
        self.current_index = 0

    def __next__(self):
        try:
            current_place = self.tourist_places[self.current_index]
            self.current_index += 1
        except IndexError:
            raise StopIteration()
        return current_place


class OwnRouteIterator(TouristPlacesIterator):
    """Iterator of tourist places at the tourist's own discretion"""
    def __init__(self, tourist_places: list):
        super().__init__(tourist_places)


class NavigatorRecommendationIterator(TouristPlacesIterator):
    """Iterator of tourist places according to the recommendations of the navigator"""
    def __init__(self, tourist_places: list):
        super().__init__(tourist_places)


class LocalGuideIterator(TouristPlacesIterator):
    """Iterator of tourist places with the help of a local guide"""
    def __init__(self, tourist_places: list):
        super().__init__(tourist_places)


class TouristPlacesCollection(Iterable):
    """Collection of tourist places"""
    def __init__(self, tourist_places: list):
        self.tourist_places = tourist_places

    def get_own_route_iterator(self) -> OwnRouteIterator:
        return OwnRouteIterator(self.tourist_places)

    def get_navigator_recommendation_iterator(self) -> NavigatorRecommendationIterator:
        return NavigatorRecommendationIterator(self.tourist_places)

    def get_local_guide_iterator(self) -> LocalGuideIterator:
        return LocalGuideIterator(self.tourist_places)

    def __iter__(self) -> OwnRouteIterator:
        return self.get_own_route_iterator()

    def add_place(self, place: any):
        self.tourist_places.append(place)
