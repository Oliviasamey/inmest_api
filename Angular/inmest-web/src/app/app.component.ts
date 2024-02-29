import { Component, OnChanges, SimpleChanges } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterOutlet } from '@angular/router';
import { FormsModule } from '@angular/forms';
import { LoginComponent } from './auth/login/login.component';
import { SideNavComponent } from './app-core/common/side-nav/side-nav.component';
import { TopNavComponent } from "./app-core/common/top-nav/top-nav.component";

@Component({
    selector: 'app-root',
    standalone: true,
    templateUrl: './app.component.html',
    styleUrl: './app.component.scss',
    imports: [CommonModule, RouterOutlet, FormsModule, LoginComponent, SideNavComponent, TopNavComponent]
})
export class AppComponent implements OnChanges{
  title = 'inmest-web';
  name = "Olivia";
  profile = {
    id: 1,
    first_name: "Olivia",
    Last_name: "SAMEY"
  }

  genesis = "hello";

  constructor() {
    console.log["constructor"]
  }
  ngOnChanges(changes: SimpleChanges): void {
    for(const inputChange in changes) {
      console.log(changes[inputChange].firstChange, inputChange);
    }
  } 
}
