import { Routes } from '@angular/router';
import { DashboardComponent } from './main-features/dashboard/dashboard.component';
import { UsersComponent } from './main-features/users/users.component';

export const routes: Routes = [
    {path:'', component: DashboardComponent},
    {path:'users', component: UsersComponent}
];
