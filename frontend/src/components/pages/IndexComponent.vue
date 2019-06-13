<template>
  <div>
    <h1>Videos</h1>
    <div class="row">
      <div class="col-md-10"></div>
      <div class = "col-md-2">
        <router-link :to="{ name : 'create'}" class="btn btn-primary">Add a Video </router-link>
      </div>
    </div><br />
    <table class="table table-hover">
      <thead>
        <tr>
          <th>
            Title
          </th>
          <th>Description</th>
          <th>File Name</th>
          <th>Delete</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(vid, index) in videos" :key="vid.index">
          <td>{{ vid.title }}</td>
          <td >{{ vid.description }}</td>
          <td>{{ vid.file }}</td>
          <td><button @click.prevent="deletevideo(vid.id, index)" class="btn btn-danger">Delete</button></td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
  export default {

    data(){
      return {
        videos : []
      }
    },
    mounted() {
    this.checkLoggedIn();
    this.created();
  },

    methods:{
      checkLoggedIn() {
      this.$session.start();
      if(!this.$session.has("token"))
        {
          this.$router.push('/');
      }   
    },

    created(){
      let token = this.$session.get("token");
      let uri = "http://localhost:8000/videos/";
      this.axios.get(uri , {headers: {Authorization: "JWT " + token}}).then(res => {
        this.videos = res.data.videos;
      })
    },
      deletevideo(id, index){
        let token = this.$session.get("token");
        let uri = "http://localhost:8000/videos/";
        this.axios.delete(uri ,{headers: {Authorization: "JWT " + token}, data: {"video_id" : id}}).then(res => {
          if (res.data.status == true){
            this.videos.splice(this.videos.indexOf(index), 1);
          }
          else{
            console.log(res.data)
          }
      });
      },
    }
  }
</script>