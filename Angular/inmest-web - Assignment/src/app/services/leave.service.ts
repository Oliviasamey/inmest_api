import { Injectable } from '@angular/core';
import { of } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class LeaveService {
  private leavesDB = [
    {
      id: 1,
      leave_type: "Maternity",
      start_date: "Dec 28, 2023",
      end_date: "Mar 28, 2024",
      created_by: "Grace",
      status: "PENDING",
      last_modified: "Nov 27, 2023",
      status_changed_by: "Derrick",
    },

    {
      id: 1,
      leave_type: "Baecation",
      start_date: " Dec 28, 2024",
      end_date: "Jan 9, 2024",
      created_by: "Suad",
      status: "PENDING",
      last_modified: "Nov 27, 2023",
      status_changed_by: "Xaari",
    }
  ];
  constructor() { }
  getLeaves() {
   return of(this.leavesDB);
  }

  getLeavebyId(id: number) {
    const leaveData = this.leavesDB.find(el => el.id === id);
    return of (leaveData);
  }
}
