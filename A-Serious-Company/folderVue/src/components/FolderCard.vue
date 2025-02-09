<template>
  <v-card class="pa-4">
    <v-row>
      <v-col cols="auto" class="d-flex justify-center align-center">
        <span class="mdi mdi-folder text-h3"></span> 
        <!-- Use text-h3 for larger size or style="font-size: 48px;" for custom size -->
      </v-col>
      <v-col>
        <v-card-title>{{ folder.title }}</v-card-title>
        <v-card-actions>
          <v-btn color="secondary" @click="$emit('edit', folder)">Edit</v-btn>
          <v-btn color="error" @click="$emit('delete', folder.id)">Delete</v-btn>
        </v-card-actions>
      </v-col>
    </v-row>
  </v-card>
</template>
  
  <script>
  export default {
    props: {
      folder: {
        type: Object,
        required: true,
      },
    },
  };
  </script>