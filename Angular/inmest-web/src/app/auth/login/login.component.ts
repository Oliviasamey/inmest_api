import { Component, OnChanges, SimpleChanges } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './login.component.html',
  styleUrl: './login.component.scss'
})
export class LoginComponent implements OnChanges{
  ngOnChanges(changes: SimpleChanges): void {
    for(const inputChange in changes) {
      console.log(changes[inputChange].firstChange, inputChange);
    }
  }
}
