class Time:
      h=0;
      m=0;
      def accept(self):
            print("enter time in hours and minutes")
            self.h=int(input())
            self.m=int(input())
      def display(self):
            print(self.h,"hours and",self.m, "minutes")
      def sum(self,t1,t2):
            self.m=t1.m+t2.m
            self.h=self.m/60
            self.m=self.m%60
            self.h=self.h+t1.h+t2.h
t1_obj=Time()
t1_obj.accept()
t2_obj=Time()
t2_obj.accept()
t3=Time()
t3.sum(t1_obj,t2_obj)
print("t1 obj")
t1_obj.display()
print("t2 obj")
t2_obj.display()
print("t3")
t3.display()   
