import { Injectable, NgModule } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Environment } from '../../../environment';

@Injectable({
  providedIn: 'root'
})

export class PontoService {

  constructor(private http: HttpClient) { }

  buscarPontos(): Observable<any> {
    return this.http.get(`${Environment.URL_BASE}/get/pontos`);
  }

  cadastrarPonto(data: { latitude: string, longitude: string }): Observable<any> {
    return this.http.post(`${Environment.URL_BASE}/register/pontos`, data);
  }

  construirMapa(): Observable<any> {
    return this.http.get(`${Environment.URL_BASE}/mapa`);
  }
}


