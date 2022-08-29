<template>
  <div class="popup">
    <p>{{ $t('download.instructions') }}</p>
    <input v-model="nameLastName" type="text" placeholder="Name and last name" ref="nameLastName" />
    <input v-model="organization" type="text" placeholder="Organization" ref="organization" />
    <input v-model="email" type="email" placeholder="your@email.example" ref="email" />
    <input v-model="country" type="text" placeholder="Country" ref="country" />
    <select v-model="role" type="text" placeholder="Role" ref="role">
      <option value="teacher">teacher</option>
      <option value="coach">coach</option>
      <option value="parent">parent</option>
      <option value="student">student</option>
    </select>
    <button @click="downloadFile">Download</button>
  </div>
</template>

<script>
export default {
  props: {
    lesson: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      nameLastName: '',
      organization: '',
      email: '',
      country: '',
      role: '',
    };
  },
  methods: {
    async downloadFile() {
      console.log('vasdfasdf');
      const downloadData = {
        name_lastname: this.nameLastName,
        organization: this.organization,
        email: this.email,
        country: this.country,
        role: this.role
      };
      const api = 'http://localhost:8000/api/v1';
      const result = await fetch(`${api}/download/`, {
        method: 'post',
        headers: {
          'content-type': 'application/json'
        },
        body: JSON.stringify(downloadData)
      });
      if (result.status === 201) {
        window.open(this.lesson.pdf);
      } else {
        alert(this.$t('download.error'));
      }
    }
  },
};
</script>

<style lang="scss" scoped>
.popup {
  width: 90vw;
  position: fixed;
  left: 5vw;
  top: 5vh;
  background-color: yellow;
  padding: 20px;
}
</style>