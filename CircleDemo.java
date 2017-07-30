class Circle
{
	double radius;
	Circle(double r)
	{
		radius=r;
	}
	double getRadius()
	{
		return radius;
	}
	double getArea()
	{
		double a=3.14*radius*radius;
		return a;
	}
	double getPerimeter()
	{
		double p=2*3.14*radius;
		return p;
	}
}
class CircleDemo
{
	public static void main(String args[])
	{
		Circle c=new Circle(5.55);
		System.out.println("the radius of the circle is"+c.getRadius());
		System.out.println("the area of the circle is"+c.getArea());
		System.out.println("the perimeter of the circle is"+c.getPerimeter());
	}
}
