package informacoesDoCaminhoDoArquivo;

import java.io.File;
import java.util.Scanner;

public class Program {

	public static void main(String[] args) {
		
		
		Scanner sc = new Scanner(System.in);
		
		
		System.out.println("Enter a folder path: ");
		String strPath = sc.nextLine();
		
		String home = System.getProperty("user.home");
		
		File path = new File(home + strPath);
		
		System.out.println("getName" + path.getName());
		System.out.println("getParent: " + path.getParent());
		System.out.println("getPath" + path.getPath());

		sc.close();
	}

}
