"""
* image.py
*
*  Created on: 25 jan. 2026
*      Author: Ludo
"""

import os

from dataclasses import dataclass

from PySide6.QtWidgets import QGraphicsScene, QGraphicsView
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

### IMAGE class ###

@dataclass
class Image:
    
    IMAGE_FILE_EXTENSION = '.jpg'

    @staticmethod
    def display(q_graphic_view: QGraphicsView, image_path: str = None) -> None:
        # Check QT object.
        if q_graphic_view is None:
            raise ValueError("No QGraphicsView provided, cannot display image")
        # Clear scene if none image is provided.
        if (image_path is None):
            q_graphic_view.setScene(None)
            return
        # Check image.
        if (not os.path.isfile(image_path)):
            raise ValueError("Image file not found:")
        # Create pixel map object.
        try:
            pixmap = QPixmap(image_path)
            if pixmap.isNull():
                raise ValueError("Failed to create pixel mapping")
            # Configure scene.
            scene = QGraphicsScene()
            scene.addPixmap(pixmap)
            scene_rect = scene.itemsBoundingRect()
            scene.setSceneRect(scene_rect)
            # Set the scene on the provided view.
            q_graphic_view.setScene(scene)
            q_graphic_view.setSceneRect(scene_rect)
            q_graphic_view.fitInView(scene_rect, Qt.KeepAspectRatio)
            q_graphic_view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            q_graphic_view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        except Exception as e:
            raise ValueError(f"Image processing failed: {e}")
        
    @staticmethod
    def clear(q_graphic_view: QGraphicsView) -> None:
        # Clear scene.
        q_graphic_view.setScene(None)
            