# Creating counstrutor
# class Rectangle


class Rectangle:
      # creating cunstructor
      def __init__(self, width, height):
            print("I'm initialising a new rectangle instance")
            self.width = width
            self.height = height
      # creating distructor
      def __del__(self):
            print("A rectangle instance is being destroyed")

rectangleToDestroy1 = Rectangle(293,117)
rectangleToDestroy2 = Rectangle(293,137)
rectangleToDestroy1 = None
rectangleToDestroy2 = None
