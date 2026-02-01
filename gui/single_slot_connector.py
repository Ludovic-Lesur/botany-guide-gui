"""
* single_slot_connector.py
*
*  Created on: 01 feb. 2026
*      Author: Ludo & Copilot
"""

import weakref
import warnings
from typing import Any, Callable, Dict, Optional

_WARNING_MSG_RE = r"Failed to disconnect .* from signal"

### SINGLE SLOT CONNECTOR classes ###

"""
* _SlotRef
* Data class containing the slot data.
"""
class _SlotRef:
    
    def __init__(self, slot: Callable):
        try:
            if hasattr(slot, "__self__") and slot.__self__ is not None:
                self._ref = weakref.WeakMethod(slot)
                self._strong = False
            else:
                self._ref = weakref.ref(slot)
                self._strong = False
        except TypeError:
            self._ref = slot
            self._strong = True

    def get(self) -> Optional[Callable]:
        if self._strong:
            return self._ref
        return self._ref()

"""
* SingleSlotConnector
* Functional class which handles single signal slot links.
"""
class SingleSlotConnector:

    def __init__(self):
        self._tracked: Dict[Any, _SlotRef] = {}

    @staticmethod
    def _safe_disconnect_all(signal: Any) -> None:
        try:
            with warnings.catch_warnings():
                warnings.filterwarnings(
                    "ignore",
                    message=_WARNING_MSG_RE,
                    category=RuntimeWarning,
                )
                signal.disconnect()
        except TypeError:
            pass
        except Exception:
            pass

    def connect(self, signal: Any, slot: Callable) -> None:
        # Check if slot is known.
        prev_ref = self._tracked.get(signal)
        if prev_ref is not None:
            prev_slot = prev_ref.get()
            if prev_slot is not None:
                try:
                    signal.disconnect(prev_slot)
                except Exception:
                    pass
            # Remove tracked entry.
            self._tracked.pop(signal, None)
        # Disconnect all.
        self._safe_disconnect_all(signal)
        # Connect new slot.
        signal.connect(slot)
        # Update track list.
        self._tracked[signal] = _SlotRef(slot)
