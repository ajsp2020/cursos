package view;

import javafx.fxml.FXML;
import javafx.scene.control.Button;

public class ViewController {
	
	@FXML
	private Button btSum;
	
	@FXML
	public void onBtSumAction() {
		System.out.println("Click");
	}
}
