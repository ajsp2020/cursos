package herdarVsCumprirContrato.model.application;

import herdarVsCumprirContrato.model.entities.AbstractShape;
import herdarVsCumprirContrato.model.entities.Circle;
import herdarVsCumprirContrato.model.entities.Rectangle;
import herdarVsCumprirContrato.model.enums.Color;

public class Program {

	
	public static void main(String[] args) {
		
		AbstractShape s1 = new Circle(Color.BLACK, 2.0);
		AbstractShape s2 = new Rectangle(Color.WHITE, 3.0, 4.0);
		
		System.out.println("Circle color: " + s1.getColor());
		System.out.println("Circle area: " + String.format("%.3f", s1.area()));
	}
}
