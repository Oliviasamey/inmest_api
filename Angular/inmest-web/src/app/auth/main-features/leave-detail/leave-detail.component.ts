import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ActivatedRoute, RouterModule } from '@angular/router';
import { LeaveService } from '../../../services/leave.service';

@Component({
  selector: 'app-leave-detail',
  standalone: true,
  imports: [CommonModule, RouterModule],
  templateUrl: './leave-detail.component.html',
  styleUrl: './leave-detail.component.scss'
})
export class LeaveDetailComponent implements OnInit{
  leaveId='';
  createdBy='';
  leave: any;
constructor(
  private route: ActivatedRoute,
  private leaveService: LeaveService
  ){}
  ngOnInit(): void {
    this.route.params.subscribe(param => {
      this.leaveId = param["id"];
    })
  }

  getMyLeaveById(id: number) {
    this.leaveService.getLeavebyId(id).subscribe(resp => {
      this.leave = resp;
      this.getMyLeaveById(parseInt(this.leaveId));
    })
  }
}

