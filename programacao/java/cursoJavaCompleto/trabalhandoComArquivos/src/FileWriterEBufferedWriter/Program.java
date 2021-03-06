package FileWriterEBufferedWriter;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;

public class Program {

	public static void main(String[] args) {
		
		String[] lines =  new String[] {"Bom dia", "Boa tarde", "Boa noite"};
		String home = System.getProperty("user.home");
		String path =  home +  "/Dropbox/antonio/Cursos/udemy/java/out.txt";

		try (BufferedWriter bw = new BufferedWriter(new FileWriter(path, true))){
			for (String line : lines) {
				bw.write(line);
				bw.newLine();
			}
		}
		catch (IOException e) {
			e.printStackTrace();
		}
		
	}

}
