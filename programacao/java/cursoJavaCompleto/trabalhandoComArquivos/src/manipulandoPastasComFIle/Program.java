package manipulandoPastasComFIle;

import java.io.File;
import java.util.Scanner;

public class Program {

	public static void main (String[] args) {

		Scanner sc = new Scanner(System.in);
		
		System.out.println("Enter a folder path: ");
		String strPath = sc.nextLine();
		
		String home = System.getProperty("user.home");
		
		File path = new File(home + strPath);
		
		File[] folders = path.listFiles(File::isDirectory);
		System.out.println("FOLDERS");
		for (File folder : folders) {
			System.out.println(folder);
		}
		
		File [] files = path.listFiles(File::isFile);
		System.out.println("FILES");
		for(File file : files) {
			System.out.println(file);
		}
		
		boolean success = new File(strPath + "/subdir").mkdir();
		System.out.println("Diretory created successfully: " + success);
		
		sc.close();
	}


}
