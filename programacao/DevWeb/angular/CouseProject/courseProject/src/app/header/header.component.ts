import { Component, EventEmitter, Output } from '@angular/core';


@Component({
  selector: 'app-header',
  templateUrl: './header.component.html'
})
export class HeaderComponent {
  @Output() featureSected= new EventEmitter<string>(); // @Output() so it can be used in the parent component

  onSelect(feature: string) {
    this.featureSected.emit(feature); // the emit method is used to emit the event
  }

}
