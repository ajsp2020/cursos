import { Component, OnInit } from '@angular/core';
import { Recipe } from '../recipe.model';

@Component({
  selector: 'app-recipe-list',
  templateUrl: './recipe-list.component.html',
  styleUrls: ['./recipe-list.component.css']
})
export class RecipeListComponent implements OnInit {
  recipes: Recipe[] = [
    new Recipe('A test Recipe', 'This is a simple a teste', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSvcQTlgu5tUcKDTDt14ZPYPWUPyjmg4AY3Aw&usqp=CAU'),
    new Recipe('A test Recipe', 'This is a simple a teste', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSvcQTlgu5tUcKDTDt14ZPYPWUPyjmg4AY3Aw&usqp=CAU')

  ];

  constructor() { }

  ngOnInit(): void {
  }

}
