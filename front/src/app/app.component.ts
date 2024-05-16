import { Component, NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { PontoService } from '../shared/services/api/Pontos/pontosService';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  standalone: true
})
export class AppComponent {
  title = 'front';

  mapaHTML = '';

  constructor(private pontoService: PontoService) { }

  ngOnInit(): void {
    this.pontoService.construirMapa().subscribe(
      (mapa: any) => {
        this.mapaHTML = mapa; // Supondo que o backend está retornando o HTML do mapa
      },
      (error) => {
        console.error('Erro ao carregar o mapa:', error);
      }
    );
  }
}

@NgModule({
  imports: [HttpClientModule], // Adicione o HttpClientModule aqui
})
export class AppModule { }
