import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment.prod';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class UserService {

  constructor(
    private http: HttpClient
  ) { }

  buscarUsers(): Observable<any> {
    return this.http.get(`${environment.URL_BASE}/consulta/user`);
  }

  cadastrarUser(data: { username: string, password: string }): Observable<any> {
    return this.http.post(`${environment.URL_BASE}/register`, data);
  }

  loginUser(data: { username: string, password: string }): Observable<any> {
    const headers = new HttpHeaders({
      'Authorization': 'Basic ' + btoa(`${data.username}:${data.password}`)
    });
    return this.http.post(`${environment.URL_BASE}/login`, {}, { headers });
  }
}
