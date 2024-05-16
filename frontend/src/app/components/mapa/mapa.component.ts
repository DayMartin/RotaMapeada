import { Component, OnInit } from '@angular/core';
import { DomSanitizer, SafeResourceUrl } from '@angular/platform-browser';
import { MapaService } from 'src/services/mapa.service';

@Component({
  selector: 'app-mapa',
  templateUrl: './mapa.component.html',
  styleUrls: ['./mapa.component.css']
})
export class MapaComponent implements OnInit {
  mapHtml: SafeResourceUrl | undefined;

  constructor(private mapService: MapaService, private sanitizer: DomSanitizer) { }

  ngOnInit(): void {
    this.mapService.construirMapa().subscribe(
      data => {
        const html = this.sanitizer.bypassSecurityTrustHtml(data);
        this.createTempHTMLFile(html);
      },
      error => console.error('Erro ao carregar o mapa:', error)
    );
  }

  createTempHTMLFile(html: SafeResourceUrl): void {
    const htmlContent = `<html><head></head><body>${html}</body></html>`;
    const blob = new Blob([htmlContent], { type: 'text/html' });
    this.mapHtml = this.sanitizer.bypassSecurityTrustResourceUrl(window.URL.createObjectURL(blob));
  }
}
