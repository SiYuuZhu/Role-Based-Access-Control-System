import axios from 'axios';

let baseUrl="http://localhost:8000/";
// create axios instances
const httpService = axios.create({
    // baseURL: process.env.BASE_API
    baseURL:baseUrl,
    timeout: 3000 
});


// add request interceptors
httpService.interceptors.request.use(function (config) {
    // GET TOKEN before send request
    config.headers.AUTHORIZATION=window.sessionStorage.getItem('token');

    return config;
}, function (error) {
    return Promise.reject(error);
});



httpService.interceptors.response.use(function (response) {
    return response;
}, function (error) {
    return Promise.reject(error);
});



//request
export function get(url, params = {}) {
    return new Promise((resolve, reject) => {
        httpService({
            url: url,
            method: 'get',
            params: params
        }).then(response => {
            resolve(response);
        }).catch(error => {
            reject(error);
        });
    });
}


export function post(url, params = {}) {
    return new Promise((resolve, reject) => {
        httpService({
            url: url,
            method: 'post',
            data: params
        }).then(response => {
            console.log(response)
            resolve(response);
        }).catch(error => {
            console.log(error)
            reject(error);
        });
    });
}


export function del(url, params = {}) {
    return new Promise((resolve, reject) => {
        httpService({
            url: url,
            method: 'delete',
            data: params
        }).then(response => {
            console.log(response)
            resolve(response);
        }).catch(error => {
            console.log(error)
            reject(error);
        });
    });
}


export function fileUpload(url, params = {}) {
    return new Promise((resolve, reject) => {
        httpService({
            url: url,
            method: 'post',
            data: params,
            headers: { 'Content-Type': 'multipart/form-data' }
        }).then(response => {
            resolve(response);
        }).catch(error => {
            reject(error);
        });
    });
}

export function getServerUrl(){
    return baseUrl;
}

export default {
    get,
    post,
    del,
    fileUpload,
    getServerUrl
}
