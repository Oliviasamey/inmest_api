import { Routes } from '@angular/router';
import { DashboardComponent } from './auth/main-features/dashboard/dashboard.component';
import { UsersComponent } from './auth/main-features/users/users.component';
import { AttendanceComponent } from './auth/main-features/attendance/attendance.component';
import { LeaveComponent } from './auth/main-features/leave/leave.component';
import { AnalyticsComponent } from './auth/main-features/analytics/analytics.component';
import { UserDetailComponent } from './auth/main-features/user-detail/user-detail.component';
import { LeaveDetailComponent } from './auth/main-features/leave-detail/leave-detail.component';

export const routes: Routes = [
    {path:'', component: DashboardComponent},
    {path:'users', component: UsersComponent},
    {path: 'attendance', component: AttendanceComponent},
    {path: 'leave', component: LeaveComponent},
    {path: 'leave/:id/:name', component: LeaveDetailComponent},
    {path: 'analytics', component: AnalyticsComponent},
    {path:'user-detail', component: UserDetailComponent}
];
