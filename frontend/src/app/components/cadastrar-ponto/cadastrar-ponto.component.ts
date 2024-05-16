import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { MapaService } from 'src/services/mapa.service';

@Component({
  selector: 'app-cadastrar-ponto',
  templateUrl: './cadastrar-ponto.component.html',
  styleUrls: ['./cadastrar-ponto.component.css']
})
export class CadastrarPontoComponent implements OnInit {
  form!: FormGroup;

  constructor(private formBuilder: FormBuilder, private mapService: MapaService) { }

  ngOnInit(): void {
    this.form = this.formBuilder.group({
      latitude: ['', Validators.required],
      longitude: ['', Validators.required]
    });
  }

  get latitude() {
    return this.form.get('latitude');
  }

  get longitude() {
    return this.form.get('longitude');
  }

  cadastrar(): void {
    if (this.form.valid) {
      const latitude = this.latitude?.value;
      const longitude = this.longitude?.value;
      this.mapService.cadastrarPonto({ latitude, longitude }).subscribe(
        response => {
          console.log('Ponto cadastrado com sucesso:', response);
          // Limpar o formulário após o cadastro bem-sucedido, se necessário
          this.form.reset();
        },
        error => {
          console.error('Erro ao cadastrar ponto:', error);
        }
      );
    }
  }

}
