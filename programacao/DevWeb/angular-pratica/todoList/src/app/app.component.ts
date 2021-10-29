import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent  {
  title = 'todoList';

  serverName = '';
  lista : string[] = [];

  constructor() {
    
  }

  onCreateList() {
    this.lista.push(this.serverName);
    this.serverName = '';
   }

   onClearList() {
     this.lista = [];
   }

}
