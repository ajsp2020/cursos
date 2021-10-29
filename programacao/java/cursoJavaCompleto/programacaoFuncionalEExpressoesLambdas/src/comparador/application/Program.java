package comparador.application;

import java.util.ArrayList;
import java.util.List;
import java.util.function.Function;
import java.util.stream.Collectors;

import comparador.entities.Product;

public class Program {

	public static void main(String[] args) {

		List<Product> list = new ArrayList<>();

		list.add(new Product("TV", 9000.00));
		list.add(new Product("Notebook", 1200.00));
		list.add(new Product("Tablet", 45.00));


		list.sort((p1, p2) ->  p1.getName().toUpperCase().compareTo(p2.getName().toUpperCase()));
		/*
		for (Product p : list) {
			System.out.println(p);
		}
		*/
		/* PREDICATE -> PricePredicate
		// Versão 1:
		//list.removeIf(p -> p.getPrice() >= 100);
		// Versão 2:
		//list.removeIf(new ProductPredicate());
		// Versao 3:
		//list.removeIf(Product :: staticProductPredicate);
		// Versao 4:
		//list.removeIf(Product :: nonStaticProductPredicate);
		// Versao 5:
		//Predicate<Product> pred = p -> p.getPrice() >= 100;
		//list.removeIf(pred);	
		
		// Inplementacao da interface
		//list.forEach(new PriceUpdate());
		
		// Reference Method com método estático
		//list.forEach(Product::staticPriceUpdate);
		 * 
		 * 	for (Product p : list) {
			System.out.println(p);
		}
		 */
		
		/* CONSUMER -> PriceUpdate
		// Reference Method com método  nãoestático
		list.forEach(Product::nonStaticPriceUpdate);
		
		list.forEach(System.out :: println);

		// Expresão lambda declarada 
		
		double factor = 1.1;
		
		Consumer<Product> cons = p -> {
			p.setPrice(p.getPrice() * factor);
		};
		list.forEach(cons);
		
		// Expressão lambda inline 
		list.forEach(p -> p.setPrice(p.getPrice() * factor));
		list.forEach(System.out :: println);
		
		*/
		
		/* FUNCTION -> UpperCaseName 
		
		List<String> names = list.stream().map(new UpperCaseName()).collect(Collectors.toList());
		names.forEach(System.out :: println);
		
		
		List<String> names = list.stream().map(Product::staticUpperCaseName).collect(Collectors.toList());
		names.forEach(System.out :: println);
	
		
		List<String> names = list.stream().map(Product::nonStaticUpperCaseName).collect(Collectors.toList());
		names.forEach(System.out :: println);
		
		Function<Product, String> func = p -> p.getName().toUpperCase();
		
		List<String> names = list.stream().map(func).collect(Collectors.toList());
		names.forEach(System.out :: println);
		
		*/
		
		List<String> names = list.stream().map(p -> p.getName().toUpperCase()).collect(Collectors.toList());
		names.forEach(System.out :: println);
		

	}

}
