#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
import random

class Algorithm:
    
    def __init__(self, image):
        self.image = image
    
    def run(self):
        '''
        custom algorithm
        '''
        
        
        # ~ cv2.imwrite("output.jpg", self.image)
        result = random.randint(0,1000)

        return result
