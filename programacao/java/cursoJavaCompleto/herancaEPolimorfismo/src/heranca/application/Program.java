package heranca.application;

import java.util.ArrayList;
import java.util.List;

import heranca.entities.Account;
import heranca.entities.BusinnesAccount;
import heranca.entities.SavingsAccount;

public class Program {

	public static void main(String[] args) {
		
		//Account acc = new Account(1001, "Alex", 0.0);
		BusinnesAccount bacc = new BusinnesAccount(1002, "Maria", 0.0, 500.0);
		
		//UPCASTING
		
		Account acc1 = bacc;
		Account acc2 = new BusinnesAccount(1003, "Bob", 0.0, 200.0);
		Account acc3 = new SavingsAccount(1004, "Anna", 0.0, 0.01);
		
		// DOWNCASTING
		
		BusinnesAccount acc4 = (BusinnesAccount)acc2;
		acc4.loan(100.0);
		
		// BusinnesAccount acc5 = (BusinnesAccount)acc3;
		
		if (acc3 instanceof BusinnesAccount) {
			BusinnesAccount acc5 = (BusinnesAccount)acc3;
			acc5.loan(200.0);
			System.out.println("Loan!");
		}
		
		if (acc3 instanceof SavingsAccount) {
			SavingsAccount acc5 = (SavingsAccount)acc3;
			acc5.updateBalance();
			System.out.println("Update!");
		}
		
		
		//Account acc6 = new Account(1001, "Alex", 1000.0);
		//acc6.withdraw(200.0);
		//System.out.println(acc6.getBalance());
		
		Account acc7 = new SavingsAccount(1002, "Maria", 1000.0, 0.01);
		acc7.withdraw(200.0);
		System.out.println(acc7.getBalance());
		
		Account acc8 = new BusinnesAccount(1003, "Bob", 1000.0, 500.0);
		acc8.withdraw(200.0);
		System.out.println(acc8.getBalance());
		
		
		List<Account> list = new ArrayList<>();
		
		list.add(new SavingsAccount(1001,"Alex", 500.0, 0.01));
		list.add(new BusinnesAccount(1002, "Maria", 1000.0, 400.0));
		list.add(new SavingsAccount(1004, "Bob", 300.0, 0.01));
		list.add(new BusinnesAccount(1005, "Anna", 500.0, 500.0));
		
		double sum = 0.0;
		for (Account acc: list) {
			sum += acc.getBalance();
		}
		
		System.out.printf("Total balance: %.2f%n", sum);
		
		for (Account acc : list) {
			acc.deposit(10.0);
		}
		
		
		for (Account acc : list) {
			System.out.printf("Updated balance for account %d: %.2f%n", acc.getNumber(), acc.getBalance());
		}

	}

}
