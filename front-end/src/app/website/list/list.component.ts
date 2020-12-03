import { Component, OnInit } from '@angular/core';
import { SharedService } from 'src/app/shared.service';

@Component({
  selector: 'app-list',
  templateUrl: './list.component.html',
  styleUrls: ['./list.component.css']
})
export class ListComponent implements OnInit {



  websites: any;
  currentWebsite: any;
  currentIndex = -1;
  name = '';

  constructor(private sharedervice: SharedService) { }

  ngOnInit(): void {
    this.listWebsites();
  }

  listWebsites(): void {
    this.sharedervice.getWebList()
      .subscribe(
        data => {
          this.websites = data;
        },
        error => {
          console.log(error);
        });
  }

  changeWebsite(e:any): void {
    this.sharedervice.getWebDetail(e.target.value)
    .subscribe(
      data => {
        this.currentWebsite = data;
        console.log(data);
      },
      error => {
        console.log(error);
      });
    }
}
