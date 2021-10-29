package comparador.util;

import java.util.function.Predicate;

import comparador.entities.Product;
// Versão 2:
public class ProductPredicate implements Predicate<Product> {

	@Override
	public boolean test(Product p) {
		return p.getPrice() >= 100;
	}
	
	
	

}
