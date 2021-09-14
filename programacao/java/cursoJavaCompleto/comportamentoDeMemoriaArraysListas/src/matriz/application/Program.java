package matriz.application;

import java.util.Scanner;

public class Program {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		int[][] mat = new int[n][n]; // Instanciando a matriz na memoria;
		
		for (int l = 0; l < mat.length; l++) {
			for (int c = 0; c < mat[l].length; c++) {
				mat[l][c] = sc.nextInt();
			}
		}
		
		System.out.println("Mai diaonal:");
		for (int i = 0; i < mat.length; i++) {
			System.out.print(mat[i][i] + " ");
		}
		
		int count = 0;
		for (int l = 0; l < mat.length; l++) {
			for (int c = 0; c < mat[l].length; c++) {
				if(mat[l][c] < 0) {
					count++;
				}
			}
		}
		
		System.out.println("Negative numbers: " + count);
		
		sc.close();
	}

}
