import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';

import { AppRoutingModule } from 'src/app-routing.module';
import { environment } from 'src/environments/environment.prod';
import { HttpClientModule} from '@angular/common/http';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations'
import { MatSlideToggleModule } from '@angular/material/slide-toggle';
import { LoginComponent } from './components/login/login.component';

import { ReactiveFormsModule } from '@angular/forms';
import { MatInputModule } from '@angular/material/input';
import { MatButtonModule } from '@angular/material/button';
import { MatCardModule } from '@angular/material/card';
import { SafeHtmlPipe } from './components/mapa/safe-html.pipe';
import { MapaComponent } from './components/mapa/mapa.component';


@NgModule({
  declarations: [AppComponent, MapaComponent, LoginComponent, SafeHtmlPipe],
  imports: [
    BrowserModule, 
    AppRoutingModule,
    HttpClientModule, 
    BrowserAnimationsModule,
    MatSlideToggleModule,
    BrowserModule,
    BrowserAnimationsModule,
    ReactiveFormsModule,
    MatInputModule,
    MatButtonModule,
    MatCardModule
  ],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
