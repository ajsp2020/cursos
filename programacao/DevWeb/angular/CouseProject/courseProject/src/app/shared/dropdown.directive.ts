import { Directive, HostBinding, HostListener } from "@angular/core";

@Directive({
    selector: "[appDropdown]"
})
export class DropdownDirective {
    @HostBinding('class.open') isOpen = false;

    @HostListener("click") toggleOpen() { //toffleOpen is a method that is called when the user clicks on the element that has the directive attached to it
        this.isOpen = !this.isOpen;
    }
}

