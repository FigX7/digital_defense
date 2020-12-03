import { Component, OnInit } from '@angular/core';
import { SharedService } from 'src/app/shared.service';

@Component({
  selector: 'app-list',
  templateUrl: './list.component.html',
  styleUrls: ['./list.component.css']
})
export class ListComponent implements OnInit {


  pages: any;
  websites: any;
  vulnerabilities: any;
  currentPage: any;
  currentWebsite: any;
  currentVulnerability: any;
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
        this.sharedervice.getPagesForSite(this.currentWebsite.id)
        .subscribe(
          pages => {
            this.pages = pages;
      },
      error => {
        console.log(error);
      });
    });
  }

  changePage(e:any): void {
    this.sharedervice.getVulnerabilitiesPath(e.target.value)
    .subscribe(
      vulnerabilities => {
        this.vulnerabilities = vulnerabilities;
    });
  }



  setActiveVulnerability(vulnerability:any, index:any): void {
    this.currentVulnerability = vulnerability;
    this.currentIndex = index;
  }

}
