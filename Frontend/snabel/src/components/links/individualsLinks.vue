<template>
  <div class="links d-flex">
    <ul>
      <li>Discover</li>
      <li>Category 1</li>
      <li>Category 1</li>
      <li>Category 1</li>
      <li>Category 1</li>
      <li>Category 1</li>
    </ul>
    <ul>
      <li>Fundaries For</li>
      <li>fund 1</li>
      <li>fund 1</li>
      <li>fund 1</li>
      <li>fund 1</li>
      <li>fund 1</li>
    </ul>
  </div>
</template>

<script>
export default {

}
</script>

<style scoped>
  .links {
    box-shadow: 2px 2px 2px 0px #aadbec96;
    background-color: #FFF;
    border-radius: 0 12px 12px 12px;
    cursor: default;
  }
  ul {
    padding: 12px;
  }
  ul:not(:last-child) {
    margin-right: 12px;
  }

  ul li:first-child {
    color: var(--mainTextColor);
    font-weight: bold;
  }
  ul li:not(:first-child) {
    padding: 4px 16px;
    margin: 0 4px;
    color: var(--mainTextColor);
    transition: .5s ease-in-out;
  }
  ul li:not(:first-child):hover {
    cursor: pointer;
    color: var(--mainColor);
    background-color: #f5f5f5;
    border-radius: 8px;
  }
</style>