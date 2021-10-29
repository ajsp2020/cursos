package metodosAbstratos.entities;

import metodosAbstratos.entities.enums.Color;

public class Circle extends Shape{
	
	private double radius;
	
	private Circle() {
		
	}
	
	public Circle(Color color, double radius) {
		super(color);
		this.radius = radius;
	}
	

	public double getRadius() {
		return radius;
	}


	public void setRadius(double radius) {
		this.radius = radius;
	}

	@Override
	public double area() {
		// TODO Auto-generated method stub
		return Math.PI * radius * radius;
	}

}
