"""
Event Priority Queue

A min-heap based priority queue for storing and retrieving events
in chronological order. Events with the same time are ordered by priority,
then by creation order for determinism.
"""

import heapq
from typing import List, Optional
from .event import Event

class EventQueue:
    """
    Priority Queue for Simulation Events.

    Internally uses heapq (min-heap) ordered by Event's natural ordering:
    (time, priority, event_id).
    """

    def __init__(self):
        self._heap: List[Event] = []
        self._event_count: int = 0

    def push(self, event: Event):
        """Add an event to the queue."""
        heapq.heappush(self._heap, event)
        self._event_count += 1

    def pop(self) -> Event:
        """
        Remove and return the next event (earliest time, highest priority).

        Raises IndexError if the queue is empty.
        """
        if not self._heap:
            raise IndexError("Cannot pop from empty event queue")
        self._event_count -= 1
        return heapq.heappop(self._heap)

    def peek(self) -> Optional[Event]:
        """Return the next event without removing it, or None if empty"""
        return self._heap[0] if self._heap else None

    def peek_time(self) -> Optional[float]:
        """Return the time of the next event, or None if empty."""
        event = self.peek()
        return event.time if event else None

    @property
    def is_empty(self) -> bool:
        """Check if the queue is empty."""
        return len(self._heap) == 0

    @property
    def size(self) -> int:
        """Return the number of event in the empty queue."""
        return len(self._heap)

    def remove(self, predicate) -> List[Event]:
        """
        Remove all the events matching a predicate function.
        Returns the list of removed events.
        This is O(n) - use sparingly.
        """
        removed = []
        kept = []
        for event in self._heap:
            if predicate(event):
                removed.append(event)
            else:
                kept.append(event)
        self._heap = kept
        heapq.heapify(self._heap)
        self._event_count = len(self._heap)
        return removed

    def clear(self):
        """Remove all events from the queue."""
        self._heap = []
        self._event_count = 0

    def __len__(self) -> int:
        return len(self._heap)

    def __repr__(self) -> str:
        return f"EventQueue(events={len(self._heap)}, next={self.peek()}"
