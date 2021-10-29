import { Directive, 
    ElementRef, 
    HostBinding, 
    HostListener, 
    Renderer2 } from "@angular/core";

@Directive({
    selector: "[appDropdown]"
})

export class DropdownDirective {
    constructor(private el: ElementRef, private renderer: Renderer2) {}
    

    @HostBinding("class.show") isOpen = false;

    changeDropdown() {
        this.isOpen = !this.isOpen;
        let part = this.el.nativeElement.querySelector(".menu-dropdown");
        if (this.isOpen) this.renderer.addClass(part, "show");
        else this.renderer.removeClass(part, "show");
    }

    @HostListener("mouseenter") toggleOpen() {
       this.changeDropdown();
    }

    @HostListener("mouseleave") toggleClose() {
        this.changeDropdown();
    }
    
}
