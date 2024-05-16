import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { MapaComponent } from './app/components/mapa/mapa.component';
import { LoginComponent } from './app/components/login/login.component';

const routes: Routes = [
  { path: 'login', component: LoginComponent },
  { path: 'mapa', component: MapaComponent },
  
];

@NgModule({
  declarations: [],
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}