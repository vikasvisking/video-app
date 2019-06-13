// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App.vue'
// import router from './router'
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css'
import VueSession from 'vue-session'
import 'bootstrap/dist/css/bootstrap.min.css'
import VueRouter from 'vue-router'
import VueAxios from 'vue-axios'
import axios from 'axios'


Vue.use(Vuetify)
Vue.use(VueSession)
Vue.use(VueRouter)
Vue.use(VueAxios, axios)
Vue.config.productionTip = false

import HomeComponent from "@/components/pages/HomeComponent.vue";
import CreateComponent from "@/components/pages/CreateComponent.vue";
import EditComponent from '@/components/pages/EditComponent.vue';
import IndexComponent from '@/components/pages/IndexComponent.vue';
import Auth from "@/components/pages/Auth.vue"

const routes = [

{
	name : "login",
	path : '/',
	component : Auth 
},

{
	name : 'create',
	path : '/create',
	component : CreateComponent
},

{
	name : 'video',
	path : '/video',
	component : IndexComponent
},
{
	name : 'edit',
	path : '/edit/:id',
	component : EditComponent
}

];

const router = new VueRouter({mode : 'history' , routes: routes});
new Vue(Vue.util.extend({router}, App)).$mount('#app');
/* eslint-disable no-new */
// new Vue({
//   el: '#app',
//   router,
//   components: { App },
//   template: '<App/>'
// })
