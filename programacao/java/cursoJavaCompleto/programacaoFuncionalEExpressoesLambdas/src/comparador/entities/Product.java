package comparador.entities;

public class Product {
	
	private String name;
	private Double price;
	
	public Product(String name, Double price) {
		this.name = name;
		this.price = price;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public Double getPrice() {
		return price;
	}

	public void setPrice(Double price) {
		this.price = price;
	}
	/* PREDICATE:
	// Versão 3:
	public static boolean staticProductPredicate(Product p) {
		return p.getPrice() >= 100;
	}
	// Versão 4:
		public boolean nonStaticProductPredicate() {
			return this.price >= 100;
		}
	*/
	
	/* CONSUMER: 	
	//Reference Method com método estático
	public static void staticPriceUpdate(Product p) {
		p.setPrice(p.getPrice() * 1.1);
	}
	
	//Reference Method com método não estático
		public void nonStaticPriceUpdate() {
			setPrice(getPrice() * 1.1);
		}
	*/
	//Reference Method com método estático
	public static String staticUpperCaseName(Product p) {
		return p.getName().toUpperCase();
	}
	
	//Reference Method com método não estático
		public  String nonStaticUpperCaseName() {
			return getName().toUpperCase();
		}

	@Override
	public String toString() {
		return "Product [name=" + name + ", price=" + price + "]";
	}
	
}
