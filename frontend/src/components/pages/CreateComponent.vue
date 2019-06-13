<template>
 <div>
  <h1> Add A new Video</h1>
  <form @submit.prevent="addVideo">
    <div class="row">
      <div class = "col-md-6">
        <div class="form-group">
          <label> Title : </label>
          <input type="text" v-model="video.title" class="form-control" required>
        </div>
      </div>
    </div>
    <div class="row">
      <div class = "col-md-6">
        <div class="form-group">
          <label> Description : </label>
          <textarea v-model="video.description" class="form-control"></textarea>
        </div>
      </div>
    </div>
    <div class="row">
      <div class = "col-md-6">
        <div class="form-group">
          <label>Video File : </label>
          <input type="file" ref="file" id="file" v-on:change="onChangeFileUpload()" placeholder="Add a video" class="form-control" required>
        </div>
      </div>
    </div>
    <br />

    <div class="form-group">
          <button  class="btn btn-primary"> Add Video</button>
    </div>
  </form>
 </div>

</template>

<script>
  export default {
    data (){
      return {
        video : {}
      }
    },
    mounted() {
    this.checkLoggedIn();
  },
    methods:{

      checkLoggedIn() {
      this.$session.start();
      if(!this.$session.has("token"))
        {
          console.log("ASdfas");
          this.$router.push('/');
      }   
    },

      addVideo(){

        let token = this.$session.get("token");
        console.log(token);
        let formData = new FormData();
        formData.append("video" , this.file);
        formData.append("title" , this.video.title);
        formData.append("description" , this.video.description);
        let uri =  "http://localhost:8000/videos/";
        this.axios.post(uri,formData, {headers: {Authorization: "JWT " + token}, 'Content-Type': 'multipart/form-data'}).then((res) =>{
          if (res.data.status == true){
            this.$router.push({name:'video'});
          }
          else{
            console.log(res.data)
          }
          
        });
      },
      onChangeFileUpload(){
        this.file = this.$refs.file.files[0];
      }
    }
  }
</script>