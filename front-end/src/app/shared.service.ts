import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class SharedService {

  readonly APIUrl = "http://127.0.0.1:8007";

  constructor(private http:HttpClient) { }

  getWebList():Observable<any[]>{
    return this.http.get<any[]>(this.APIUrl + '/websites/');
  }

  getWebDetail(id:any):Observable<any[]>{
    return this.http.get<any[]>(this.APIUrl + '/websites/' + id + '/');
  }
}
