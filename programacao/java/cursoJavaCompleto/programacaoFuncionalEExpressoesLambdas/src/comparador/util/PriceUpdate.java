package comparador.util;

import java.util.function.Consumer;

import comparador.entities.Product;


// Implementacao da interface
public class PriceUpdate implements Consumer<Product>{

	@Override
	public void accept(Product p) {
		 p.setPrice(p.getPrice() * 1.1);
		
	}
	
	

}
