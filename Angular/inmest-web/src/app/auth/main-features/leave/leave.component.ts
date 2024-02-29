import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { LeaveService } from '../../../services/leave.service';

@Component({
  selector: 'app-leave',
  standalone: true,
  imports: [CommonModule, RouterModule],
  templateUrl: './leave.component.html',
  styleUrl: './leave.component.scss'
})
export class LeaveComponent {
  leave: any[] = [];

  constructor(
    private leaveService: LeaveService
  ) {}

  ngOnInit(): void{
    this.getLeaves();
  }

  getLeaves() {
    this.leaveService.getLeaves().subscribe((resp: any) => {
      this.leave = resp;
    })
  }
  
}
