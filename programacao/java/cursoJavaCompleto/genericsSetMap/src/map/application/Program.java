package map.application;

import java.util.Map;
import java.util.TreeMap;

public class Program {
	
	public static void main(String[] args) {
		
		Map<String, String> cookies = new TreeMap<>();
		
		
		cookies.put("username", "Maria");
		cookies.put("email", "maria@gmail.com");
		cookies.put("phone", "99999999");
		cookies.remove("email");
		
		System.out.println("Contains 'phone' key: " + cookies.containsKey("phone"));
		System.out.println("Phone number: " + cookies.get("phone"));
		System.out.println("Size: " + cookies.size());

		
		for (String key : cookies.keySet()) {
			System.out.println(key + ": " + cookies.get(key));
		}
		
	}
	
}
