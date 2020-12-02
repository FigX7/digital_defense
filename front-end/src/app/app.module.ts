import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { WebsiteComponent } from './website/website.component';
import { ListComponent } from './website/list/list.component';

import { SharedService } from 'src/app/shared.service';


@NgModule({
  declarations: [
    AppComponent,
    WebsiteComponent,
    ListComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [SharedService],
  bootstrap: [AppComponent]
})
export class AppModule { }
