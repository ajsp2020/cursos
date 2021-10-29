module javafx2 {
	requires javafx.controls;
	requires javafx.fxml;
	
	opens applicatio to javafx.graphics, javafx.fxml;
	opens view to javafx.fxml;

}
